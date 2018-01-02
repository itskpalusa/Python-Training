CREATE TABLE [Books] (
    [Title] NVARCHAR(150) PRIMARY KEY NOT NULL,
    [Author] NVARCHAR(50) NOT NULL,
    [ISBN] INTEGER RAND(1000,5000) NOT NULL,
);
INSERT INTO Books VALUES(1, 'Harry Potter and the Order of the Phoenix', 'J.K. Rowling', RAND(1000,5000));


CREATE TABLE [User] (
    [StudentId] INTEGER  PRIMARY KEY NOT NULL,
    [StudentName] NVARCHAR(50) NOT NULL,
);
INSERT INTO Students VALUES(1, 'Michael');
INSERT INTO Students VALUES(2, 'John');
INSERT INTO Students VALUES(3, 'Jack');
INSERT INTO Students VALUES(4, 'Sara');
INSERT INTO Students VALUES(5, 'Sally');
INSERT INTO Students VALUES(6, 'Jena');
INSERT INTO Students VALUES(7, 'Nancy');

CREATE TABLE [Date] (
  [Date] DATETIME

)
