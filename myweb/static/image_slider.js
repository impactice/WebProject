document.addEventListener('DOMContentLoaded', function() {
    const sliderContainer = document.querySelector('.image-slider-container');
    const slider = document.querySelector('.image-slider');
    const prevButton = document.querySelector('.prev-button');
    const nextButton = document.querySelector('.next-button');
    const images = slider.querySelectorAll('img');
    const imageCount = images.length;
    let currentIndex = 0;
    let intervalId;
    const autoSlideInterval = 10000; // 10초마다 자동 슬라이드

    function updateSlider() {
        const translateX = -currentIndex * 100 + '%';
        slider.style.transform = 'translateX(' + translateX + ')';
    }

    function nextSlide() {
        currentIndex = (currentIndex + 1) % imageCount;
        updateSlider();
    }

    function prevSlide() {
        currentIndex = (currentIndex - 1 + imageCount) % imageCount;
        updateSlider();
    }

    function startAutoSlide() {
        intervalId = setInterval(nextSlide, autoSlideInterval);
    }

    function stopAutoSlide() {
        clearInterval(intervalId);
    }

    if (prevButton && nextButton) {
        prevButton.addEventListener('click', () => {
            stopAutoSlide();
            prevSlide();
            startAutoSlide();
        });

        nextButton.addEventListener('click', () => {
            stopAutoSlide();
            nextSlide();
            startAutoSlide();
        });
    }

    // 마우스 호버 시 자동 슬라이드 멈춤, 벗어나면 다시 시작 (선택 사항)
    if (sliderContainer) {
        sliderContainer.addEventListener('mouseenter', stopAutoSlide);
        sliderContainer.addEventListener('mouseleave', startAutoSlide);
    }

    startAutoSlide(); // 초기 자동 슬라이드 시작
});