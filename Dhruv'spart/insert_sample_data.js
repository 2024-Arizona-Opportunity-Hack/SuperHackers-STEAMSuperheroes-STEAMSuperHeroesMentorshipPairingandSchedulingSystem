const { MongoClient } = require('mongodb');
require('dotenv').config();

const uri = process.env.MONGO_URI;
const dbName = 'hackathon_project';

async function insertSampleData() {
  const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

  try {
    await client.connect();
    const db = client.db(dbName);

    const mentor = {
      email: 'astrogirl2448@gmail.com',
      name: { first: 'Swati', last: 'Mohan' },
      age: '40-50',
      availability: {
        Monday: ['7pm to 9pm'],
        Tuesday: ['7pm to 9pm'],
        Wednesday: ['3pm to 5pm', '5pm to 7pm']
      },
      location: { city: 'Glendale', state: 'CA' },
      role: 'Mentor',
    };

    const mentee = {
      email: 'mentee001@gmail.com',
      name: { first: 'John', last: 'Doe' },
      age: '20-30',
      availability: {
        Monday: ['7pm to 9pm'],
        Tuesday: ['7pm to 9pm'],
        Wednesday: ['3pm to 5pm', '5pm to 7pm']
      },
      location: { city: 'Los Angeles', state: 'CA' },
      role: 'Mentee',
    };

    await db.collection('mentors').insertOne(mentor);
    await db.collection('mentees').insertOne(mentee);
    console.log('Sample data inserted successfully');
  } finally {
    await client.close();
  }
}

insertSampleData();
