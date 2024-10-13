import React from 'react';
import MatchedPairs from './MatchedPairs';
import UpcomingMeetings from './UpcomingMeetings';
import ProfileManagement from './ProfileManagement';
import Notifications from './Notifications';

const Dashboard = () => {
    return (
        <div className="dashboard">
            <MatchedPairs />
            <UpcomingMeetings />
            <ProfileManagement />
            <Notifications />
        </div>
    );
};

export default Dashboard;
