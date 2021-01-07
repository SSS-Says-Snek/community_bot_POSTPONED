CREATE TABLE IF NOT EXISTS members (
    id BIGINT PRIMARY KEY,
    username VARCHAR(35) NOT NULL,
    discriminator INT,
    overall_infractions INT,
    audit_log_infractions INT,
    bot_banned BOOL
    -- role_uid INT
);

CREATE TABLE IF NOT EXISTS roles (
    member_id BIGINT,
    role_id BIGINT,
    role_name VARCHAR(40),
    member_name VARCHAR(35),
    PRIMARY KEY (member_id, role_id)
);

CREATE TABLE IF NOT EXISTS guilds (
    guild_id BIGINT PRIMARY KEY,
    prefix VARCHAR(8),
    guild_name VARCHAR(35),
    num_members INT,
    num_roles INT
);

SELECT * FROM members;
SELECT * FROM roles;
SELECT * FROM guilds;
