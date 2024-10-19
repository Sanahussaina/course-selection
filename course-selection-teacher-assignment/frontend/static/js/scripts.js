document.addEventListener('DOMContentLoaded', function () {
    // Sample data for courses and teachers (to be replaced with actual data from the server)
    const courses = {
        theory: [
            { id: 1, name: "Data Structures" },
            { id: 2, name: "Algorithms" },
            { id: 3, name: "Database Management Systems" },
            { id: 4, name: "Operating Systems" },
            { id: 5, name: "Software Engineering" },
            { id: 6, name: "Web Development" },
            { id: 7, name: "Artificial Intelligence" },
            { id: 8, name: "Machine Learning" }
        ],
        lab: [
            { id: 9, name: "Data Structures Lab" },
            { id: 10, name: "Algorithms Lab" },
            { id: 11, name: "Database Lab" },
            { id: 12, name: "Web Development Lab" },
            { id: 13, name: "AI Lab" }
        ]
    };

    const teachers = {
        1: [
            { id: 1, name: "Dr. Smith", rating: 4.5, profile: "Expert in data structures and algorithms." },
            { id: 2, name: "Prof. Johnson", rating: 4.7, profile: "Specializes in algorithms and AI." }
        ],
        2: [
            { id: 3, name: "Dr. Brown", rating: 4.8, profile: "Expert in database management systems." },
            { id: 4, name: "Prof. Wilson", rating: 4.6, profile: "Specialized in web development." }
        ],
        3: [
            { id: 5, name: "Dr. Taylor", rating: 4.9, profile: "Specializes in machine learning." },
            { id: 6, name: "Prof. Harris", rating: 4.4, profile: "Expert in operating systems." }
        ],
        4: [
            { id: 7, name: "Dr. Clark", rating: 4.7, profile: "Expert in software engineering." },
            { id: 8, name: "Prof. Lee", rating: 4.5, profile: "Specialized in web technologies." },
            { id: 9, name: "Dr. Kim", rating: 4.6, profile: "Expert in AI." }
        ],
        // Add teachers for other courses similarly...
    };

    // Populate courses in the course selection form
    function populateCourses() {
        const theoryCoursesDiv = document.getElementById('theory-courses');
        const labCoursesDiv = document.getElementById('lab-courses');

        // Add theory courses
        courses.theory.forEach(course => {
            const courseLabel = document.createElement('label');
            courseLabel.innerHTML = `
                <input type="checkbox" name="theory" value="${course.id}">
                ${course.name}
            `;
            theoryCoursesDiv.appendChild(courseLabel);
        });

        // Add lab courses
        courses.lab.forEach(course => {
            const courseLabel = document.createElement('label');
            courseLabel.innerHTML = `
                <input type="checkbox" name="lab" value="${course.id}">
                ${course.name}
            `;
            labCoursesDiv.appendChild(courseLabel);
        });
    }

    // Handle course selection and display corresponding teachers
    function handleCourseSelection() {
        const selectedTheoryCheckboxes = document.querySelectorAll('input[name="theory"]:checked');
        const selectedLabCheckboxes = document.querySelectorAll('input[name="lab"]:checked');

        const selectedCourses = [...selectedTheoryCheckboxes, ...selectedLabCheckboxes].map(cb => cb.value);

        const teacherSelectionDiv = document.getElementById('teacher-selection');
        teacherSelectionDiv.innerHTML = ""; // Clear previous selections

        selectedCourses.forEach(courseId => {
            const teacherLabel = document.createElement('div');
            teacherLabel.innerHTML = `
                <h3>Teachers for Course ID ${courseId}:</h3>
                <select name="teacher_${courseId}">
                    <option value="">Select a teacher</option>
                    ${teachers[courseId]?.map(teacher => `<option value="${teacher.id}">${teacher.name} (Rating: ${teacher.rating})</option>`).join('') || ""}
                </select>
            `;
            teacherSelectionDiv.appendChild(teacherLabel);
        });
    }

    // Add event listeners
    document.getElementById('theory-courses').addEventListener('change', handleCourseSelection);
    document.getElementById('lab-courses').addEventListener('change', handleCourseSelection);

    // Call the function to populate courses when the page loads
    populateCourses();
});
