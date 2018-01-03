CREATE TABLE [Books] (
    [Title] NVARCHAR(150) PRIMARY KEY NOT NULL,
    [Author] NVARCHAR(50) NOT NULL,
    [ISBN] INTEGER RAND(1000,5000) NOT NULL,
);
INSERT INTO Books VALUES(1, 'Harry Potter and the Order of the Phoenix', 'J.K. Rowling', RAND(1000,5000));

CREATE TABLE [User] (
    [SchoolId] INTEGER  PRIMARY KEY NOT NULL,
    [Name] NVARCHAR(50) NOT NULL,
    [Usertype] VARCHAR(6) NOT NULL CHECK (Usertype IN ('Student', 'Staff')),
);
INSERT INTO User VALUES(1, 'Michael');
INSERT INTO User VALUES(2, 'John');
INSERT INTO User VALUES(3, 'Jack');
INSERT INTO User VALUES(4, 'Sara');
INSERT INTO User VALUES(5, 'Sally');
INSERT INTO User VALUES(6, 'Jena');
INSERT INTO User VALUES(7, 'Nancy');

CREATE TABLE [Loans] (
  [loanDate] DATETIME
  [dueDate] loanDate + loan_time(user)

)
