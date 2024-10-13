const fs = require('fs');
const path = require('path');
const { google } = require('googleapis');
const readline = require('readline');

const CREDENTIALS_PATH = path.join(__dirname, 'credentials.json');
const TOKEN_PATH = path.join(__dirname, 'token.json');

// Load client secrets from a local file.
function authorize() {
  const credentials = JSON.parse(fs.readFileSync(CREDENTIALS_PATH));
  const { client_secret, client_id, redirect_uris } = credentials.installed;
  const oAuth2Client = new google.auth.OAuth2(client_id, client_secret, redirect_uris[0]);

  // Check if we have previously stored a token.
  if (fs.existsSync(TOKEN_PATH)) {
    const token = fs.readFileSync(TOKEN_PATH);
    oAuth2Client.setCredentials(JSON.parse(token));
    return oAuth2Client;
  } else {
    return getAccessToken(oAuth2Client);
  }
}

// Get and store new token after prompting for user authorization
function getAccessToken(oAuth2Client) {
  const authUrl = oAuth2Client.generateAuthUrl({
    access_type: 'offline',
    scope: ['https://www.googleapis.com/auth/calendar'],
  });
  console.log('Authorize this app by visiting this url:', authUrl);
  
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  rl.question('Enter the code from that page here: ', (code) => {
    rl.close();
    oAuth2Client.getToken(code, (err, token) => {
      if (err) return console.error('Error retrieving access token', err);
      oAuth2Client.setCredentials(token);

      // Store the token to disk for later program executions
      fs.writeFileSync(TOKEN_PATH, JSON.stringify(token));
      console.log('Token stored to', TOKEN_PATH);

      return oAuth2Client;
    });
  });
}

// Function to create a Google Calendar event
async function createCalendarEvent(auth, eventDetails) {
  const calendar = google.calendar({ version: 'v3', auth });

  const event = {
    summary: 'Mentorship Meeting',
    description: 'A meeting between mentor and mentee',
    start: {
      dateTime: eventDetails.startTime,
      timeZone: 'America/Los_Angeles',
    },
    end: {
      dateTime: eventDetails.endTime,
      timeZone: 'America/Los_Angeles',
    },
    attendees: [
      { email: eventDetails.mentorEmail },
      { email: eventDetails.menteeEmail },
    ],
  };

  try {
    const response = await calendar.events.insert({
      calendarId: 'primary',
      resource: event,
    });
    console.log('Event created: %s', response.data.htmlLink);
  } catch (err) {
    console.error('Error creating calendar event:', err);
  }
}

module.exports = { authorize, createCalendarEvent };
