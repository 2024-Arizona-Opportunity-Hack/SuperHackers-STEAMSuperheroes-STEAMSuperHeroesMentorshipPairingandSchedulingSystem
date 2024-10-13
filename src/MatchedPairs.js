import React from 'react';

const MatchedPairs = () => {
    const pairs = [{ mentor: 'John Doe', mentee: 'Jane Smith' }];

    return (
        <div className="card">
            <h2>Matched Pairs</h2>
            {pairs.map((pair, index) => (
                <div key={index}>
                    <strong>Mentor:</strong> {pair.mentor} | <strong>Mentee:</strong> {pair.mentee}
                </div>
            ))}
        </div>
    );
};

export default MatchedPairs;
