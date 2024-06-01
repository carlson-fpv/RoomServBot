let tg = window.Telegram.WebApp;

tg.expand();

tg.MainButton.text.Color = '#FFFFFF';
tg.MainButton.color = '#2cab37';
tg.MainButton.setText('Вы выбрали солянку');

var item = '';
var items_count = [0, 0, 0];
var item_0_btn = document.getElementById('item_0_btn');
var item_1_btn = document.getElementById('item_1_btn');
var item_2_btn = document.getElementById('item_2_btn');
var item_0_decr_btn = document.getElementById('item_0_decrement');
var item_0_incr_btn = document.getElementById('item_0_increment');

const quanityControls = document.querySelector('.quanity-controls');
const btnClass = document.querySelector('.btn');

item_0_btn.addEventListener('click', function(){
  if (tg.MainButton.isVisible) {
    tg.MainButton.hide();
  }
  else {
    tg.MainButton.setText('Вы выбрали солянку');
    item = '0';
    tg.MainButton.show();
  }
  items_count[0] += 1;
  document.getElementById('item_0_counter').innerHTML = items_count[0];
  btnClass.style.display = 'none';
  quanityControls.style.display = 'inline-block';
});

item_0_decr_btn.addEventListener('click', function() {
  if (items_count[0] > 0) {
    items_count[0] -= 1;
  }
  if (items_count[0] == 0) {
    btnClass.style.display = 'inline-block';
    quanityControls.style.display = 'none';
  }
  document.getElementById('item_0_counter').innerHTML = items_count[0];
});

item_0_incr_btn.addEventListener('click', function() {
  items_count[0] += 1;
  document.getElementById('item_0_counter').innerHTML = items_count[0];
});

item_1_btn.addEventListener('click', function(){
  if (tg.MainButton.isVisible) {
    tg.MainButton.hide();
  }
  else {
    tg.MainButton.setText('Вы выбрали картофель');
    item = '1';
    tg.MainButton.show();
  }
});

item_2_btn.addEventListener('click', function(){
  if (tg.MainButton.isVisible) {
    tg.MainButton.hide();
  }
  else {
    tg.MainButton.setText('Вы выбрали шницель');
    item = '2';
    tg.MainButton.show();
  }
});

Telegram.WebApp.onEvent('mainButtonClicked', function() {
  tg.sendData(item);
})
