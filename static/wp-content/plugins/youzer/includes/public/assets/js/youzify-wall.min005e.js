var youzify_load_attachments=!1;!function(n){"use strict";n(document).ready(function(){jQuery().viewportChecker&&(n.youzify_init_wall_posts_effect=function(){n(".youzify_effect")[0]&&n(".youzify_effect").viewportChecker({classToAdd:"animated",classToRemove:"invisible",removeClassAfterAnimation:!0,offset:"10%",callbackFunction:function(t,i){t.addClass(t.data("effect"))}},500)},n.youzify_init_wall_posts_effect(),n("#youzify div.activity")[0]&&new MutationObserver(function(t){n.youzify_init_wall_posts_effect(),n.youzify_sliders_init()}).observe(n("#youzify div.activity")[0],{attributes:!1,childList:!0,subtree:!0,characterData:!1}));if(n(document).on("click",".youzify-trigger-who-modal",function(t){t.preventDefault();var i=n(this);if(!i.hasClass("loading")){i.addClass("loading");var a=!1;if(!i.find("i").get(0)){var o=i.text();a=!0;i.html('<i class="fas fa-spin fa-spinner"></i>')}var e=n(this).closest("li.activity-item"),s={action:n(this).data("action"),post_id:e.attr("id").substr(9,e.attr("id").length)};jQuery.post(Youzify.ajax_url,s,function(t){a&&i.html(o),n.youzify_show_modal(n(t)),i.removeClass("loading")})}}),n(document).on("click",".youzify-delete-post",function(t){var i=n(this),a=i.parents("div.activity ul li"),o=a.prop("class").match(/date-recorded-([0-9]+)/);i.addClass("loading"),jq.post(ajaxurl,{action:"delete_activity",cookie:bp_get_cookies(),id:n(this).parent().attr("data-activity-id"),_wpnonce:i.attr("data-nonce")},function(t){t[0]+t[1]==="-1"?(a.prepend(t.substr(2,t.length)),a.children("#message").hide().fadeIn(300)):(a.slideUp(300),o&&activity_last_recorded===o[1]&&(newest_activities="",activity_last_recorded=0))})}),n(document).on("click",".youzify-show-tagged-users",function(t){t.preventDefault(),n(".youzify-wall-modal-overlay").fadeIn(500,function(){n(this).find(".youzify-modal-loader").fadeIn(400)});var i=n(this).closest("li.activity-item"),a={action:"youzify_activity_tagged_users_modal",post_id:i.attr("id").substr(9,i.attr("id").length)};jQuery.post(Youzify.ajax_url,a,function(t){n("#youzify-wall-modal").append(t).find(".youzify-wall-modal").addClass("youzify-wall-modal-show"),n(".youzify-wall-modal-overlay").find(".youzify-modal-loader").hide()})}),n(document).keyup(function(t){n(".youzify-wall-modal-show")[0]&&27===t.keyCode&&n(".youzify-wall-modal-close").trigger("click")}),n(document).mouseup(function(t){n(".youzify-wall-modal-overlay").is(t.target)&&n(".youzify-wall-modal-show")[0]&&n(".youzify-wall-modal-close").trigger("click")}),"on"==Youzify.activity_autoloader){var a=n(window);a.scroll(function(){var t=n("#activity-stream .load-more:visible");if(t.get(0)&&!t.data("youzify-autoloaded")){var i=t.offset().top-3e3;a.scrollTop()+a.height()>i&&(t.data("youzify-autoloaded",1),t.find("a").trigger("click"))}})}n("#activity-stream").on("click",".friendship-button a",function(){n(this).parent().addClass("loading");var t=n(this).attr("id"),i=n(this).attr("href"),o=n(this);return t=(t=t.split("-"))[1],i=(i=(i=i.split("?_wpnonce="))[1].split("&"))[0],jq.post(ajaxurl,{action:"addremove_friend",cookie:bp_get_cookies(),fid:t,_wpnonce:i},function(t){var i=o.attr("rel"),a=o.parent();"add"===i?n(a).fadeOut(200,function(){a.removeClass("add_friend"),a.removeClass("loading"),a.addClass("pending_friend"),a.fadeIn(200).html(t)}):"remove"===i&&n(a).fadeOut(200,function(){a.removeClass("remove_friend"),a.removeClass("loading"),a.addClass("add"),a.fadeIn(200).html(t)})}),!1}),n("#activity-stream").on("click",".group-button a",function(t){n(this).hasClass("membership-requested")||n(this).addClass("youzify-btn-loading");var i=n(this).parent().attr("id"),a=n(this).attr("href"),e=n(this);return i=(i=i.split("-"))[1],a=(a=(a=a.split("?_wpnonce="))[1].split("&"))[0],e.hasClass("leave-group")&&!1===confirm(BP_DTheme.leave_group_confirm)||jq.post(ajaxurl,{action:"joinleave_group",cookie:bp_get_cookies(),gid:i,_wpnonce:a},function(a){var o=e.parent();n(o).fadeOut(200,function(){o.fadeIn(200).html(a);var t=n("#groups-personal span"),i=1;e.hasClass("leave-group")?(o.hasClass("hidden")&&o.closest("li").slideUp(200),i=0):e.hasClass("request-membership")&&(i=!1),t.length&&!1!==i&&(i?t.text(1+(t.text()>>0)):t.text((t.text()>>0)-1))})}),!1}),n("audio,video").on("play",function(){n("audio,video").not(this).each(function(t,i){i.pause()}),n("iframe").each(function(t,i){n(i).attr("src",n(i).attr("src"))})}),n(document).on("click",".nice-select .option",function(t){n(this).parent().prev(".current").attr("data-value",n(this).attr("data-value"))}),n("#activity-stream").on("click","li.load-more",function(t){if(n(this).closest(".youzify-activity-shortcode")[0]){t.stopImmediatePropagation();var i=n(this);i.addClass("loading");var a=n(this).parents(".youzify-activity-shortcode");a.attr("data-page",parseInt(a.attr("data-page"))+1);var o=a.data();return o.page=a.attr("data-page"),n.post(ajaxurl,{data:o,action:"youzify_activity_load_activities"},function(t){t.success&&(i.hide(),i.parents("ul.activity-list").append(t.data))},"json"),!1}}),n(document).on("click",".activity-item .youzify-show-item-tools",function(t){var i=n(this),a=i.closest("li.activity-item"),o=i.find("i").attr("class");i.hasClass("loaded")?a.find(".youzify-activity-tools").fadeToggle():i.hasClass("loading")||(i.addClass("loading"),i.find("i").attr("class","fas fa-spin fa-spinner"),n.ajax({type:"POST",url:ajaxurl,dataType:"json",data:{activity_id:a.attr("id").substr(9,a.attr("id").length),action:"youzify_get_activity_tools"},success:function(t){i.find("i").attr("class",o),i.addClass("loaded"),i.removeClass("loading"),t.success&&n(t.data).prependTo(a).fadeIn(),n(t.data).find(".youzify-pin-tool").get(0)&&n("<script/>",{rel:"text/javascript",src:Youzify.assets+"js/youzify-sticky-posts.min.js"}).appendTo("head"),n(t.data).find(".youzify-bookmark-tool").get(0)&&n("<script/>",{rel:"text/javascript",src:Youzify.assets+"js/youzify-bookmark-posts.min.js"}).appendTo("head")}}))}),n(".youzify-activity-show-search-form").on("click",function(t){t.preventDefault();var i=n(this);i.closest("ul").find("#activity-filter-select .youzify-dropdown-area").fadeOut(1,function(){i.closest("li").find(".youzify-dropdown-area").fadeToggle(),i.closest("li").find("input").focus()})}),n(".youzify-activity-show-filter").on("click",function(t){t.preventDefault();var i=n(this);i.closest("ul").find(".youzify-activity-show-search .youzify-dropdown-area").fadeOut(1,function(){i.closest("li").find(".youzify-dropdown-area").fadeToggle()})}),n(".youzify-show-activity-search").on("click",function(t){t.preventDefault();var i=n(this).parents("#youzify"),a=i.find(".youzify-activity-show-search .youzify-dropdown-area");i.find("#activity-filter-select .youzify-dropdown-area, .activity-type-tabs").fadeOut(),a.fadeToggle(),a.find("input").focus()}),n(".youzify-show-activity-filter").on("click",function(t){t.preventDefault();var i=n(this).parents("#youzify");i.find(".youzify-activity-show-search .youzify-dropdown-area, .activity-type-tabs").fadeOut(),i.find("#activity-filter-select .youzify-dropdown-area").fadeToggle()}),n(".youzify-show-activity-menu").on("click",function(t){t.preventDefault();var i=n(this).parents("#youzify");i.find("#subnav .youzify-dropdown-area").fadeOut(),i.find(".activity-type-tabs").fadeToggle()}),n(".activity_share").on("click",".activity-read-more a",function(t){var i=n(this);return i.addClass("loading"),n.post(ajaxurl,{action:"get_single_activity_content",activity_id:i.parent().attr("id").split("-")[3]},function(t){i.closest(".activity-inner").slideUp(300).html(t).slideDown(300)}),!1}),n(document).on("click",".youzify-wall-modal-close",function(t){t.preventDefault(),n(".youzify-wall-modal").removeClass("youzify-wall-modal-show"),n(".youzify-wall-modal-overlay").fadeOut(600),setTimeout(function(){n(".youzify-wall-modal").remove()},500)})})}(jQuery);