jQuery(document).ready(function($) {
  if( $('.multiple-file-upload').length > 0 ) {
    var itemTemplate = $('#mfu-item-template');
    var itemsContainer = $('#mfu-items-container');
    var itemNumber = 1;
    
    createMfuItem(itemTemplate, itemsContainer, itemNumber);
    itemNumber++;
    
    $('#mfu-new-item-btn').click(function(e) {
      createMfuItem(itemTemplate, itemsContainer, itemNumber);
      itemNumber++;
    });
  }
});

function createMfuItem(itemTemplate, itemsContainer, itemNumber) {
  itemTemplateHtml = itemTemplate.html().replace(/\{ITEM_NUMBER\}/g, itemNumber);
  itemsContainer.append( itemTemplateHtml );
}


$("body").on('click', '.mfuDeleteBtn', function(e) {
  console.log($(e.target).attr('data-send'));
  $.ajax({
    method: "POST",
    url: $(e.target).attr('data-url'),
    data: $(e.target).attr('data-send')
  })
  .done(function( msg ) {
    $(e.target).closest('.forDelete').find('.server-response').html(msg).show();
    var activitySelectWrap = $(e.target).closest(".forDelete");
    activitySelectWrap.remove();
  })
  .fail(function() {
    $(e.target).closest('.forDelete').find('.server-response').html('Ошибка удаления').show();
  });
});