Base Meerkat API
================


get_leaderboard(print_flag = True)
----------------------------------

get_live_broadcasts(print_flag = True)
--------------------------------------

get_scheduled_broadcasts(print_flag = True)
-------------------------------------------

get_broadcast_summary(broadcast_id, print_flag = True)
------------------------------------------------------

get_broadcast_watchers(broadcast_id, print_flag = True)
------------------------------------------------------

get_broadcast_restreams(broadcast_id, print_flag = True)
------------------------------------------------------

get_broadcast_likes(broadcast_id, print_flag = True)
------------------------------------------------------

get_broadcast_comments(broadcast_id, print_flag = True)
------------------------------------------------------

get_broadcast_activities(broadcast_id, print_flag = True)
------------------------------------------------------

get_broadcast_stream_link(broadcast_id)
------------------------------------------------------

save_live_stream(broadcast_id, delay_milliseconds, num_images, output_dir, display = True)
------------------------------------------------------

play_live_stream(broadcast_id, audio = True, video = True)
----------------------------------------------------------

kill_live_stream()
-------------------

get_user_profile(user_id, print_flag = True)
---------------------------------------------