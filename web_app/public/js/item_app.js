document.addEventListener('DOMContentLoaded', () => {
  let tg = window.Telegram.WebApp;
  tg.expand();
  tg.BackButton.show();
  tg.BackButton.onClick(back_button_callback);

  const url_param = new URLSearchParams(window.location.search);
  const item_id = url_param.get('id');
  const app_type = url_param.get('type');
  console.log(app_type);
  var total_amount = url_param.get('amount');
  //console.log('amount: ', total_amount, ' ', total_amount > 0, ' ', typeof(total_amount));
  var price = 0;
  var temp_amount = 0;
  if (total_amount == 'null') {
    total_amount = 0;
    //console.log(typeof(total_amount));
  } else {
    total_amount = parseInt(total_amount);
    //console.log(typeof(total_amount));
  }
  var count = 0;
  const item_btn = document.getElementById('item_price');
  const item_decr_btn = document.getElementById('item_decrement');
  const item_incr_btn = document.getElementById('item_increment');
  const item_btn_class = document.querySelector('.btn#item_price');
  const quanity_controls = document.querySelector('.quanity_controls');
  const apply_btn = document.getElementById('apply_btn');
  const apply_btn_class = document.querySelector('.btn#apply_btn');

  fetch('../data/' + app_type + '/items.json')
    .then(response => response.json())
    .then(items => {
      const item = items.find(itm => itm.id == item_id);
      if (item) {
        document.getElementById('item_name').textContent = item.item_name;
        document.getElementById('item_image').src = item.item_image;
        document.getElementById('item_description').textContent = item.item_description;
        document.getElementById('item_price').textContent = "Цена: " + item.item_price.toString();
        price = item.item_price;
        //console.log('price: ', typeof(price), ' ', price);
      }
    })
    .catch(error => console.error('Error fetching items data: ', error));

    item_btn_class.addEventListener('click', () => {
      count += 1;
      temp_amount += price;
      item_btn_class.style.display = 'none';
      quanity_controls.style.display = 'inline-block';
      apply_btn_class.style.display = 'inline-block';
      //console.log(typeof(temp_amount), ' ', temp_amount);
      document.getElementById('item_counter').innerHTML = temp_amount;
    });

    item_decr_btn.addEventListener('click', () => {
      if (count > 0) {
        count -= 1;
        temp_amount -= price;
      }
      if (count == 0) {
        item_btn_class.style.display = 'inline-block';
        quanity_controls.style.display = 'none';
        apply_btn_class.style.display = 'none';
      }
      document.getElementById('item_counter').innerHTML = temp_amount;
    });

    item_incr_btn.addEventListener('click', () => {
      count += 1;
      temp_amount += price;
      document.getElementById('item_counter').innerHTML = temp_amount;
    });

    apply_btn.addEventListener('click', () => {
      temp_amount += total_amount;
      window.location.href = 'magazine.html?amount=' + temp_amount + '&type=' + app_type;
    });

    function back_button_callback() {
      temp_amount += total_amount;
      window.location.href = 'magazine.html?amount=' + temp_amount + '&type=' + app_type;
    };
});