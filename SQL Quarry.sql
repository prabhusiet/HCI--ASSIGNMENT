CREATE DATABASE PassITDrivingSchool;
USE PassITDrivingSchool;

CREATE TABLE Instructors (
    InstructorID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    ContactNumber VARCHAR(15)
);

CREATE TABLE Students (
    StudentID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    ContactNumber VARCHAR(15),
    Email VARCHAR(255)
);

CREATE TABLE Lessons (
    LessonID INT AUTO_INCREMENT PRIMARY KEY,
    InstructorID INT,
    StudentID INT,
    LessonType VARCHAR(50),
    LessonDate DATETIME,
    DurationHours INT,
    FOREIGN KEY (InstructorID) REFERENCES Instructors(InstructorID),
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID)
);

##Data Impoting 

INSERT INTO Instructors (FirstName, LastName, ContactNumber) VALUES
('John', 'Doe', '1234567890'),
('Jane', 'Smith', '2345678901'),
('Alice', 'Johnson', '3456789012'),
('Bob', 'Lee', '4567890123'),
('Carol', 'Taylor', '5678901234'),
('David', 'Brown', '6789012345'),
('Emma', 'Davis', '7890123456'),
('Frank', 'Miller', '8901234567'),
('Grace', 'Wilson', '9012345678'),
('Henry', 'Moore', '0123456789'),
('Ivy', 'Taylor', '1234509876'),
('Jack', 'Smith', '2345619870'),
('Kathy', 'Lee', '3456721981'),
('Louis', 'Clark', '4567832192'),
('Maria', 'Lewis', '5678943213'),
('Nathan', 'Walker', '6789054324'),
('Olivia', 'Allen', '7890165435'),
('Peter', 'Young', '8901276546'),
('Queen', 'Harris', '9012387657'),
('Rachel', 'Nelson', '0123498768');

INSERT INTO Students (FirstName, LastName, ContactNumber, Email) VALUES
('Alex', 'Gordon', '9234567890', 'alex.gordon@example.com'),
('Betty', 'White', '8345678901', 'betty.white@example.com'),
('Charlie', 'Green', '7456789012', 'charlie.green@example.com'),
('Daisy', 'Black', '6567890123', 'daisy.black@example.com'),
('Ethan', 'King', '5678901234', 'ethan.king@example.com'),
('Fiona', 'Knight', '4789012345', 'fiona.knight@example.com'),
('George', 'Lee', '3890123456', 'george.lee@example.com'),
('Hannah', 'Scott', '2901234567', 'hannah.scott@example.com'),
('Irene', 'Carter', '1012345678', 'irene.carter@example.com'),
('James', 'Phillips', '2123456789', 'james.phillips@example.com'),
('Kara', 'Evans', '3234567890', 'kara.evans@example.com'),
('Leo', 'Parker', '4345678901', 'leo.parker@example.com'),
('Mia', 'Edwards', '5456789012', 'mia.edwards@example.com'),
('Noah', 'Collins', '6567890123', 'noah.collins@example.com'),
('Olga', 'Stewart', '7678901234', 'olga.stewart@example.com'),
('Pablo', 'Sanchez', '8789012345', 'pablo.sanchez@example.com'),
('Quinn', 'Morris', '9890123456', 'quinn.morris@example.com'),
('Ruby', 'Cook', '0901234567', 'ruby.cook@example.com'),
('Steven', 'Bailey', '2012345678', 'steven.bailey@example.com'),
('Tina', 'Rivera', '3123456789', 'tina.rivera@example.com');

INSERT INTO Lessons (InstructorID, StudentID, LessonType, LessonDate, DurationHours) VALUES
(1, 1, 'Introductory', '2024-05-10 10:00:00', 2),
(2, 2, 'Standard', '2024-05-11 11:00:00', 1),
(3, 3, 'Pass Plus', '2024-05-12 09:00:00', 3),
(4, 4, 'Driving Test', '2024-05-13 14:00:00', 2),
(5, 5, 'Introductory', '2024-05-14 10:00:00', 1),
(1, 6, 'Standard', '2024-05-15 13:00:00', 2),
(2, 7, 'Pass Plus', '2024-05-16 08:00:00', 3),
(3, 8, 'Driving Test', '2024-05-17 15:00:00', 1),
(4, 9, 'Introductory', '2024-05-18 11:00:00', 2),
(5, 10, 'Standard', '2024-05-19 16:00:00', 1),
(1, 11, 'Pass Plus', '2024-05-20 09:30:00', 3),
(2, 12, 'Driving Test', '2024-05-21 13:00:00', 2),
(3, 13, 'Introductory', '2024-05-22 10:00:00', 1),
(4, 14, 'Standard', '2024-05-23 14:00:00', 2),
(5, 15, 'Pass Plus', '2024-05-24 08:00:00', 3),
(1, 16, 'Driving Test', '2024-05-25 15:00:00', 2),
(2, 17, 'Introductory', '2024-05-26 11:00:00', 1),
(3, 18, 'Standard', '2024-05-27 09:00:00', 2),
(4, 19, 'Pass Plus', '2024-05-28 13:00:00', 3),
(5, 20, 'Driving Test', '2024-05-29 16:00:00', 1);




