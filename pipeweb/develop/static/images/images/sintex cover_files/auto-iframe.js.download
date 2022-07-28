function AutoiFrameAdjustiFrameHeight( id, fudge )
      {
      var frame = document.getElementById( id );
	  
	  if( frame == null ) { return; }
	  if( frame.contentDocument == null ) { return; }
	  if( frame.contentDocument.body == null ) { return; }
	  
      var content = jQuery('.embed-wrap');
      var height = frame.contentDocument.body.offsetHeight + fudge;

      content.height( height );
      frame.height = height;
      }
