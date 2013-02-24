// Toggle control for bigger footer
  this.toggleBiggerFooter = function(e) {
    e.preventDefault();

    var speed = 500,
        $firstFooter = $('.first-footer'),
        $evenBiggerFooter = $('p.even-bigger-footer');
      
    if(_gaq) {
      _gaq.push(['_trackPageview', 'Bigger Footer']);
    }  
    
    $('footer').find('div.bigger-footer').slideToggle(speed);
    $firstFooter.toggleClass('open');
    if ($evenBiggerFooter.hasClass('open')) {
      $('footer p.even-bigger-footer').trigger('click');
    }
    
    
    if (!$('body').hasClass('fourofour')) {
      $('html, body').animate({
        scrollTop: $(document).height()
      }, speed);
    }
  };
  
  // Toggle control for even bigger footer
  this.toggleEvenBiggerFooter = function(e) {
    e.preventDefault();

    var speed = 200,
        $evenBiggerFooter = $('p.even-bigger-footer');
    
    if(_gaq) {
      _gaq.push(['_trackPageview', 'Even Bigger Footer']);
    }
        
    $('footer').find('div.even-bigger-footer').slideToggle(speed);
    $evenBiggerFooter.toggleClass('open');
 
    $('html, body').animate({
      scrollTop: $(document).height()
    }, speed);
  };
  