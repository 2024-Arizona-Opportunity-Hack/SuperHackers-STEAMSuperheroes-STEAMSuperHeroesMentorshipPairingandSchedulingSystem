import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCalendarAlt } from '@fortawesome/free-solid-svg-icons';

const UpcomingMeetings = () => {
    const meetings = [
        { date: '2024-10-15', time: '3:00 PM', details: 'First meeting with John Doe' },
        { date: '2024-10-22', time: '4:00 PM', details: 'Follow-up with Jane Smith' },
    ];

    return (
        <div className="card">
            <h2>
                <FontAwesomeIcon icon={faCalendarAlt} /> Upcoming Meetings
            </h2>
            {meetings.map((meeting, index) => (
                <div key={index}>
                    <strong>Date:</strong> {meeting.date} | <strong>Time:</strong> {meeting.time} | <strong>Details:</strong> {meeting.details}
                </div>
            ))}
        </div>
    );
};

export default UpcomingMeetings;
