var btn = document.querySelector('div.add-btn');
var list = document.querySelector('div.add-list');

var items = document.querySelector('div.items');
var notes = document.querySelector('div.notes');
var tasks = document.querySelector('div.tasks');

var fade = document.querySelector('div.fade.one');
var fadeTwo = document.querySelector('div.fade.two');
var btnLeft = document.querySelector('div.left-slide');
var btnRight = document.querySelector('div.right-slide');

var btnSide = document.querySelector('button.side-layout');
var btnScroll = document.querySelector('button.scroll-layout');


btn.addEventListener('click', function () {
  list.classList.toggle("show");
})

btnLeft.addEventListener('click', function () {
  if (items.classList.contains('right')) {
    items.classList.remove('right')
    notes.classList.add('active')
    tasks.classList.remove('active')
  } else {
    return null
  }
})

btnRight.addEventListener('click', function () {
  items.classList.add('right')
  notes.classList.remove('active')
  tasks.classList.add('active')
})

btnSide.addEventListener('click', function () {
  if (items.classList.contains('scroll')) {
    btnScroll.classList.remove('active')
    btnSide.classList.add('active')
    items.classList.remove('scroll')
    fade.classList.add('hide')
    fadeTwo.classList.add('hide');
    notes.classList.remove('active')
    tasks.classList.remove('active')
  } else {
    return null
  }
})

btnScroll.addEventListener('click', function () {
  if (items.classList.contains('scroll')) {
    return null
  } else {
    btnSide.classList.remove('active')
    btnScroll.classList.add('active')
    items.classList.add('scroll');
    items.classList.remove('right');
    notes.classList.add('active');
    fade.classList.remove('hide');
    fadeTwo.classList.remove('hide');
  }
})