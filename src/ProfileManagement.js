import React, { useState } from 'react';

const ProfileManagement = () => {
    const [profile, setProfile] = useState({
        name: 'John Doe',
        email: 'john.doe@example.com',
        role: 'Mentor',
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setProfile({ ...profile, [name]: value });
    };

    return (
        <div className="card">
            <h2>Profile Management</h2>
            <form>
                <label>
                    Name:
                    <input type="text" name="name" value={profile.name} onChange={handleChange} style={{ margin: '10px 0', width: '100%' }} />
                </label>
                <label>
                    Email:
                    <input type="email" name="email" value={profile.email} onChange={handleChange} style={{ margin: '10px 0', width: '100%' }} />
                </label>
                <label>
                    Role:
                    <input type="text" name="role" value={profile.role} onChange={handleChange} style={{ margin: '10px 0', width: '100%' }} />
                </label>
                <button type="submit" style={{ backgroundColor: '#007bff', color: '#ffffff', border: 'none', padding: '10px', borderRadius: '5px' }}>
                    Update Profile
                </button>
            </form>
        </div>
    );
};

export default ProfileManagement;
