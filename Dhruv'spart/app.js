// Importing necessary modules
require('dotenv').config(); // Load environment variables from .env
const { connectDB } = require('./db'); // MongoDB connection
const { generateMeetingDates, suggestMeetingTimes } = require('./scheduler'); // Scheduler logic
const { authorize, createCalendarEvent } = require('./calendar'); // Google Calendar authorization and event creation
const { sendEmailNotification } = require('./notifications'); // Email notification logic
const moment = require('moment'); // Date handling library

// Main function to run the app
async function runApp() {
  try {
    // Connect to MongoDB
    const db = await connectDB();

    // Fetch mentor and mentee data from MongoDB collection
    const mentor = await db.collection('mentors').findOne({ email: 'astrogirl2448@gmail.com' });
    const mentee = await db.collection('mentees').findOne({ email: 'mentee001@gmail.com' });

    // Check if mentor or mentee was not found in the database
    if (!mentor || !mentee) {
      console.log('Mentor or mentee not found');
      return;
    }

    // Task 1: Suggest meeting times based on availability of mentor and mentee
    const suggestedTimes = suggestMeetingTimes(mentor.availability, mentee.availability);
    console.log('Suggested meeting times:', suggestedTimes);

    // Select the first available time for simplicity (you can adjust this as needed)
    const [day, times] = Object.entries(suggestedTimes)[0];
    const timeSlot = times[0];

    // Task 2: Generate meeting dates (e.g., weekly meetings for 4 occurrences)
    const meetingDates = generateMeetingDates(moment().day(day), 'weekly', 4);
    console.log('Generated meeting dates:', meetingDates);

    // Task 3: Create Google Calendar events for each meeting date
    const auth = await authorize(); // Authorize Google Calendar API

    for (const date of meetingDates) {
      const eventDetails = {
        mentorEmail: mentor.email,
        menteeEmail: mentee.email,
        startTime: date,
        endTime: moment(date).add(1, 'hour').format() // 1-hour meeting duration
      };
      await createCalendarEvent(auth, eventDetails); // Create Google Calendar event
    }

    // Task 4: Send email notifications to mentor and mentee with the meeting schedule
    const message = `Your mentorship meetings have been scheduled on the following dates: ${meetingDates.join(', ')}`;
    await sendEmailNotification(mentor.email, 'Mentorship Meeting Schedule', message);
    await sendEmailNotification(mentee.email, 'Mentorship Meeting Schedule', message);

  } catch (error) {
    console.error('Error running the application:', error);
  }
}

// Run the application
runApp();
