DROP TABLE IF EXISTS data;

CREATE TABLE data (
    trn_id INTEGER PRIMARY KEY,
    created_at DATE,
    amount INTEGER,
    ref_id VARCHAR(255),
    type TEXT,
    trn_date DATE,
    UNIQUE(ref_id)
);
