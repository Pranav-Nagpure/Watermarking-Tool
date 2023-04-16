var options = document.getElementById('radiofield');
var img_watermark_option = document.getElementById('img_watermark_option');
var txt_watermark_option = document.getElementById('txt_watermark_option');

var wm_img_div = document.getElementById('wm_img_div');
var wm_txt_div = document.getElementById('wm_txt_div');

var img_upload = document.getElementById('img_upload');
var wm_img_upload = document.getElementById('wm_img_upload');
var wm_txt_upload = document.getElementById('wm_txt_upload');
var submit_button = document.getElementById('submit_button');

var result_img = document.getElementById('result_img');

function submit_button_disable() {
  if (img_upload.value != '' && ((img_watermark_option.checked && wm_img_upload.value != '') || (txt_watermark_option.checked && wm_txt_upload.value != ''))) {
    submit_button.disabled = false;
  }
  else {
    submit_button.disabled = true;
  }
}

options.onchange = function () {
  if (img_watermark_option.checked) {
    wm_img_div.style.display = 'block';
    wm_txt_div.style.display = 'none';
  }
  else if (txt_watermark_option.checked) {
    wm_img_div.style.display = 'none';
    wm_txt_div.style.display = 'block';
  }
  submit_button_disable();
}

img_upload.onchange = submit_button_disable;
wm_img_upload.onchange = submit_button_disable;
wm_txt_upload.oninput = submit_button_disable;

if (result_img.getAttribute('src') == '') {
  result_img.style.display = 'none';
}