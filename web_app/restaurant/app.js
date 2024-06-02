let tg = window.Telegram.WebApp;

//tg.expand();

tg.MainButton.text.Color = '#FFFFFF';
tg.MainButton.color = '#2cab37';
tg.BackButton.show();

var items_count = [0, 0, 0];
var items_costs = [400, 150, 700];
var amount = 0;

var item_0_btn = document.getElementById('item_0_btn');
var item_1_btn = document.getElementById('item_1_btn');
var item_2_btn = document.getElementById('item_2_btn');
var item_0_decr_btn = document.getElementById('item_0_decrement');
var item_0_incr_btn = document.getElementById('item_0_increment');
var item_1_decr_btn = document.getElementById('item_1_decrement');
var item_1_incr_btn = document.getElementById('item_1_increment');
var item_2_decr_btn = document.getElementById('item_2_decrement');
var item_2_incr_btn = document.getElementById('item_2_increment');

const quanity_controls_0 = document.querySelector('.quanity-controls#item_0_qc');
const quanity_controls_1 = document.querySelector('.quanity-controls#item_1_qc');
const quanity_controls_2 = document.querySelector('.quanity-controls#item_2_qc');
const btn_class_0 = document.querySelector('.btn#item_0_btn');
const btn_class_1 = document.querySelector('.btn#item_1_btn');
const btn_class_2 = document.querySelector('.btn#item_2_btn');

// Обработаем нажатие на кнопку первого продукта
item_0_btn.addEventListener('click', function(){
  items_count[0] += 1;
  amount += items_costs[0];
  document.getElementById('item_0_counter').innerHTML = items_count[0];
  btn_class_0.style.display = 'none';
  quanity_controls_0.style.display = 'inline-block';
  console.log('items_count[0]=' + items_count[0] + ', amount=' + amount);
  tg.MainButton.setText('Оплатить ' + amount + 'P');
  tg.MainButton.show();
});

// Обработаем нажатие на кнопку уменьшения количества товара
item_0_decr_btn.addEventListener('click', function() {
  if (items_count[0] > 0) {
    items_count[0] -= 1;
    amount -= items_costs[0];
    if (amount > 0) {
      tg.MainButton.setText('Оплатить ' + amount + 'р');
    }
    else {
      tg.MainButton.hide();
    }
  }
  if (items_count[0] == 0) {
    btn_class_0.style.display = 'inline-block';
    quanity_controls_0.style.display = 'none';
  }
  document.getElementById('item_0_counter').innerHTML = items_count[0];
});

// Обработаем нажатие на кнопку увеличения количества товара
item_0_incr_btn.addEventListener('click', function() {
  items_count[0] += 1;
  amount += items_costs[0];
  document.getElementById('item_0_counter').innerHTML = items_count[0];
  tg.MainButton.setText('Оплатить ' + amount + 'P');
});

// Обработаем нажатие на кнопку второго товара
item_1_btn.addEventListener('click', function(){
  items_count[1] += 1;
  amount += items_costs[1];
  document.getElementById('item_1_counter').innerHTML = items_count[1];
  btn_class_1.style.display = 'none';
  quanity_controls_1.style.display = 'inline-block';
  console.log('items_count[1]=' + items_count[1] + ', amount=' + amount);
  tg.MainButton.setText('Оплатить ' + amount + 'P');
  tg.MainButton.show();
});

// Обработаем нажатие на кнопку уменьшения количества товара
item_1_decr_btn.addEventListener('click', function() {
  if (items_count[1] > 0) {
    items_count[1] -= 1;
    amount -= items_costs[1];
    if (amount > 0) {
      tg.MainButton.setText('Оплатить ' + amount + 'р');
    }
    else {
      tg.MainButton.hide();
    }
  }
  if (items_count[1] == 0) {
    btn_class_1.style.display = 'inline-block';
    quanity_controls_1.style.display = 'none';
  }
  document.getElementById('item_1_counter').innerHTML = items_count[1];
});

// Обработаем нажатие на кнопку увеличения количества товара
item_1_incr_btn.addEventListener('click', function() {
  items_count[1] += 1;
  amount += items_costs[1];
  document.getElementById('item_1_counter').innerHTML = items_count[1];
  tg.MainButton.setText('Оплатить ' + amount + 'P');
});

// Обработаем нажатие на кнопку третьего товара
item_2_btn.addEventListener('click', function(){
  items_count[2] += 1;
  amount += items_costs[2];
  document.getElementById('item_2_counter').innerHTML = items_count[2];
  btn_class_2.style.display = 'none';
  quanity_controls_2.style.display = 'inline-block';
  console.log('items_count[2]=' + items_count[2] + ', amount=' + amount);
  tg.MainButton.setText('Оплатить ' + amount + 'P');
  tg.MainButton.show();
});

// Обработаем нажатие на кнопку уменьшения количества товара
item_2_decr_btn.addEventListener('click', function() {
  if (items_count[2] > 0) {
    items_count[2] -= 1;
    amount -= items_costs[2];
    if (amount > 0) {
      tg.MainButton.setText('Оплатить ' + amount + 'р');
    }
    else {
      tg.MainButton.hide();
    }
  }
  if (items_count[2] == 0) {
    btn_class_2.style.display = 'inline-block';
    quanity_controls_2.style.display = 'none';
  }
  document.getElementById('item_2_counter').innerHTML = items_count[2];
});

// Обработаем нажатие на кнопку увеличения количества товара
item_2_incr_btn.addEventListener('click', function() {
  items_count[2] += 1;
  amount += items_costs[2];
  document.getElementById('item_2_counter').innerHTML = items_count[2];
  tg.MainButton.setText('Оплатить ' + amount + 'P');
});

Telegram.WebApp.onEvent('mainButtonClicked', function() {
  console.log("Preparing to send amout=" + amount);
  tg.sendData(amount.toString());
});
