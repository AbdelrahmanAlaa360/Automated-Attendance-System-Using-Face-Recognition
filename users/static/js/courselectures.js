const attendanceView  = document.querySelector('.lecture .btn');
attendanceView.addEventListener('click', () => {
  window.open('attendance.html', 'newPage', 'height=400,width=800,resizable=no,top=100,left=200');
});