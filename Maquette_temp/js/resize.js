    calculateAspectRatioFit : function(f, maxWidth, maxHeight) {

        srcWidth = f.width
        srcHeight = f.height
        
        var ratio = [maxWidth / srcWidth, maxHeight / srcHeight ];
        ratio = Math.min(ratio[0], ratio[1]);
        
        f.width ==ratio[0]
        f.height == ratio[1]
     }