const nodemailer = require('nodemailer');
require('dotenv').config(); // Load environment variables from .env

// Function to send email notifications
const sendEmailNotification = async (to, subject, text) => {
  // Create a transporter object using SMTP transport
  const transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
      user: process.env.EMAIL_USER, // Your Gmail email address from .env
      pass: process.env.EMAIL_PASS  // Your app-specific password from .env
    }
  });

  // Define mail options (recipient, subject, and message body)
  const mailOptions = {
    from: process.env.EMAIL_USER, // sender address
    to: to,                       // list of recipients
    subject: subject,             // subject line
    text: text                    // plain text body
  };

  // Send the email
  try {
    let info = await transporter.sendMail(mailOptions);
    console.log('Email sent: ' + info.response);
  } catch (error) {
    console.error('Error sending email:', error);
  }
};

module.exports = { sendEmailNotification };
