document.getElementById('radiofield').onchange = function() {
    if(document.getElementById('img_watermark_option').checked) {
      document.getElementById('wm_img_div').style.display = 'block';
      document.getElementById('wm_txt_div').style.display = 'none';
    }else if(document.getElementById('txt_watermark_option').checked) {
      document.getElementById('wm_img_div').style.display = 'none';
      document.getElementById('wm_txt_div').style.display = 'block';
    }
  }