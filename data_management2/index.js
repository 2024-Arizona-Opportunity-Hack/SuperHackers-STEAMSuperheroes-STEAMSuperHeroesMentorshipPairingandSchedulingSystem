const { MongoClient } = require('mongodb');

// MongoDB URI - Change to your connection string if using MongoDB Atlas
const uri = 'mongodb://localhost:27017';

async function createMentor() {
  const client = new MongoClient(uri, { useUnifiedTopology: true });

  try {
    await client.connect();  // Connect to MongoDB
    const db = client.db('hackathon');  // Create or access a database called 'hackathon'
    const mentors = db.collection('mentors');  // Create 'mentors' collection

    // Insert a mentor document
    const mentor = {
      name: 'John Doe',
      age: 35,
      location: 'California',
      availability: {
        Monday: ['7pm to 9pm'],
        Wednesday: ['3pm to 5pm'],
      },
      preferences: {
        ethnicity: 'Prefer it, but available to others',
        gender: 'Prefer it, but available to others',
      },
    };

    const result = await mentors.insertOne(mentor);
    console.log(`Mentor inserted with ID: ${result.insertedId}`);
  } finally {
    await client.close();  // Close the connection
  }
}

// Call the function to create a mentor
createMentor().catch(console.error);

async function scheduleMeeting(pairingId, sessionId, meetings) {
    const client = new MongoClient(uri, { useUnifiedTopology: true });
  
    try {
      await client.connect();
      const db = client.db('hackathon');
      const meetingsCollection = db.collection('meetings');
  
      // Insert meeting schedule
      const result = await meetingsCollection.insertOne({
        pairingId: pairingId,
        sessionId: sessionId,
        meetings: meetings  // Array of meetings
      });
  
      console.log(`Meeting scheduled with ID: ${result.insertedId}`);
    } finally {
      await client.close();
    }
  }
  
 
  
  async function updateMeetingStatus(pairingId, meetingDate, newStatus) {
    const client = new MongoClient(uri, { useUnifiedTopology: true });
  
    try {
      await client.connect();
      const db = client.db('hackathon');
      const meetingsCollection = db.collection('meetings');
  
      // Update the status of a specific meeting
      const result = await meetingsCollection.updateOne(
        { pairingId: pairingId, "meetings.date": meetingDate },
        { $set: { "meetings.$.status": newStatus } }
      );
  
      console.log(`Meeting on ${meetingDate} updated to status: ${newStatus}`);
    } finally {
      await client.close();
    }
  }
  
 

  async function generateMeetingReport(sessionId) {
    const client = new MongoClient(uri, { useUnifiedTopology: true });
  
    try {
      await client.connect();
      const db = client.db('hackathon');
      const meetingsCollection = db.collection('meetings');
  
      const report = await meetingsCollection.aggregate([
        { $match: { sessionId: sessionId } },
        { $unwind: "$meetings" },
        { $group: {
            _id: "$meetings.status",
            count: { $sum: 1 }
        }}
      ]).toArray();
  
      console.log('Meeting Report:', report);
    } finally {
      await client.close();
    }
  }
  

  
  const createCsvWriter = require('csv-writer').createObjectCsvWriter;

async function exportMeetingsToCSV(sessionId) {
  const client = new MongoClient(uri, { useUnifiedTopology: true });

  try {
    await client.connect();
    const db = client.db('hackathon');
    const meetingsCollection = db.collection('meetings');

    const meetings = await meetingsCollection.find({ sessionId: sessionId }).toArray();

    const csvWriter = createCsvWriter({
      path: 'meetings_report.csv',
      header: [
        { id: '_id', title: 'ID' },
        { id: 'pairingId', title: 'Pairing ID' },
        { id: 'sessionId', title: 'Session ID' },
        { id: 'meetings', title: 'Meetings' }
      ]
    });

    await csvWriter.writeRecords(meetings);
    console.log('Data exported to meetings_report.csv');
  } finally {
    await client.close();
  }
}


