document.addEventListener('DOMContentLoaded', () => {
  let tg = window.Telegram.WebApp;
  tg.MainButton.text.Color = '#FFFFFF';
  tg.MainButton.color = '#2cab37';
  tg.BackButton.show();
  tg.BackButton.onClick(back_button_callback);const items = document.querySelectorAll('.item');

  const url_param = new URLSearchParams(window.location.search);
  const app_type = url_param.get('type');

  fetch('data/app_pages.json')
    .then(response => response.json())
    .then(pages => {
      const page = pages.find(pge => pge.type == app_type);
      if (page) {
        document.getElementById('item_0_img').src = page.item_0_img;
        document.getElementById('item_0_img').alt = page.item_0_name;
        document.getElementById('item_0_name').textContent = page.item_0_name + ' ' + page.item_0_price + 'р';
        document.getElementById('item_1_img').alt = page.item_1_name;
        document.getElementById('item_1_img').src = page.item_1_img;
        document.getElementById('item_1_name').textContent = page.item_1_name + ' ' + page.item_1_price + 'р';
        document.getElementById('item_2_img').alt = page.item_2_name;
        document.getElementById('item_2_img').src = page.item_2_img;
        document.getElementById('item_2_name').textContent = page.item_2_name + ' ' + page.item_2_price + 'р';
      }
    })

  var amount = url_param.get('amount');
  console.log('current amount: ', amount);
  if (amount > 0) {
        tg.MainButton.setText('Оплатить ' + amount + 'р');
        tg.MainButton.show();
  }

  Telegram.WebApp.onEvent('mainButtonClicked', function() {
    console.log("Preparing to send amout=" + amount);
    tg.sendData(amount.toString());
  });

  items.forEach(item => {
    item.addEventListener('click', () => {
      const itemID = item.getAttribute('id');
      console.log('Attaching this id at URL: ', itemID + ' ' + app_type);
      window.location.href = 'item.html?id=' + itemID + '&amount=' + amount + '&type=' + app_type;
    });
  });

  function back_button_callback() {
    tg.close();
  };
});