import React from 'react';

const Notifications = () => {
    const notifications = [
        { message: 'Reminder: Meeting with Jane Smith on 2024-10-15', type: 'reminder' },
        { message: 'Cancellation: Meeting with John Doe on 2024-10-22', type: 'cancellation' },
    ];

    return (
        <div className="card">
            <h2>Notifications</h2>
            {notifications.map((notification, index) => (
                <div key={index} className={`notification ${notification.type}`}>
                    {notification.message}
                </div>
            ))}
        </div>
    );
};

export default Notifications;
