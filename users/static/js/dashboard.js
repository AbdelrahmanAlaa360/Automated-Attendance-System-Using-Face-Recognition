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



  const div = document.getElementsByClassName('course');
  const text = document.getElementsByClassName('text');

  const checkTextOverflow = () => {
    const containerWidth = div.offsetWidth;
    const textWidth = text.offsetWidth;
    const fontSize = parseInt(window.getComputedStyle(text).fontSize);

    if (textWidth > containerWidth) {
      const newFontSize = fontSize - 1;
      text.style.fontSize = newFontSize + 'px';
      checkTextOverflow();
    }
  };

  checkTextOverflow();

});


