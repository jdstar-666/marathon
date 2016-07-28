/**
* @Author: lisnb
* @Date:   2016-07-28T05:03:42+08:00
* @Email:  lisnb.h@hotmail.com
* @Last modified by:   lisnb
* @Last modified time: 2016-07-28T05:04:33+08:00
*/



/*!
 * Star Rating Chinese Translations
 *
 * This file must be loaded after 'star-rating.js'. Patterns in braces '{}', or
 * any HTML markup tags in the messages must not be converted or translated.
 *
 * NOTE: this file must be saved in UTF-8 encoding.
 *
 * @see http://github.com/kartik-v/bootstrap-star-rating
 * @author Kartik Visweswaran <kartikv2@gmail.com>
 * @author Freeman
 */
 (function ($) {
    "use strict";
    $.fn.ratingLocales['zh'] = {
        defaultCaption: '{rating} 星',
        starCaptions: {
            0.5: '半星',
            1: '1分',
            1.5: '一星半',
            2: '2分',
            2.5: '二星半',
            3: '3分',
            3.5: '三星半',
            4: '4分',
            4.5: '四星半',
            5: '5分'
        },
        clearButtonTitle: '清除',
        clearCaption: '0分'
    };
})(window.jQuery);
