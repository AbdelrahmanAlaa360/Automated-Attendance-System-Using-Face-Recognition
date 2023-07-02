document.addEventListener("DOMContentLoaded", () => {
  const scrollContainer = document.getElementsByClassName("courses")[0];
  const scrollLeftButton = document.getElementsByClassName("left-arrow")[0];
  const scrollRightButton = document.getElementsByClassName("right-arrow")[0];

  scrollLeftButton.addEventListener("click", () => {
    scrollContainer.scrollBy({
      left: -260,
      behavior: "smooth",
    });
  });

  scrollRightButton.addEventListener("click", () => {
    scrollContainer.scrollBy({
      left: 260,
      behavior: "smooth",
    });
  });


  function updateProgress(value,  name) {
    const progressBar = document.querySelector(name);
    progressBar.style.width = value + '%';
  }
  
  updateProgress(45,'.progress1'); // sets progress to 50%
  updateProgress(15,'.progress2');
  updateProgress(25,'.progress3');
  
  const createCourseButton = document.querySelector('#newCourse');
  createCourseButton.addEventListener('click', () => {
    window.open('CourseCreation.html', 'newPage', 'height=700,width=800,resizable=no,top=50,left=400');
  });
  
  const lecturesView = document.querySelector('.course .text');
  lecturesView.addEventListener('click', () => {
    window.open('courselectures.html', 'newPage', 'height=600,width=800,resizable=no,top=100,left=200');
  
  });
  
  const attendanceView  = document.querySelector('#btn');
  attendanceView.addEventListener('click', () => {
    window.open('attendance.html', 'newPage', 'height=400,width=800,resizable=no,top=100,left=200');
    
  });
  


});


