let tg = window.Telegram.WebApp;

tg.expand();

tg.MainButton.text.Color = "#FFFFFF";
tg.MainButton.color = "#2cab37";
tg.MainButton.setText("Вы выбрали солянку");

let item = "";

let btn1 = document.getElementById("btn1");
let btn2 = document.getElementById("btn2");
let btn3 = document.getElementById("btn3");

btn1.addEventListener("click", function(){
  if (tg.MainButton.isVisible) {
    tg.MainButton.hide();
  }
  else {
    tg.MainButton.setText("Вы выбрали солянку");
    item = "1";
    tg.MainButton.show();
  }
});

btn2.addEventListener("click", function(){
  if (tg.MainButton.isVisible) {
    tg.MainButton.hide();
  }
  else {
    tg.MainButton.setText("Вы выбрали картофель");
    item = "2";
    tg.MainButton.show();
  }
});

btn3.addEventListener("click", function(){
  if (tg.MainButton.isVisible) {
    tg.MainButton.hide();
  }
  else {
    tg.MainButton.setText("Вы выбрали шницель");
    item = "3";
    tg.MainButton.show();
  }
});

Telegram.WebApp.onEvent("mainButtonClicked", function() {
  tg.sendData(item);
})
