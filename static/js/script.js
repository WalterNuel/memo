var btn = document.querySelector('div.add-btn');
var list = document.querySelector('div.add-list');

btn.addEventListener('click', function () {
  list.classList.toggle("show");
})