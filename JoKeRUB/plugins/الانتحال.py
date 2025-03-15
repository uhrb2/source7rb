@l313l.ar_cmd(pattern="انتحال(?:\s|$)([\s\S]*)")
async def _(event):
    mid = await l313l.get_me()
    me = (await event.client(GetFullUserRequest(mid.id))).full_user
    replied_user, error_i_a = await get_user_from_event(event)
    if replied_user is None:
        return await edit_delete(event, "**يجب الرد على رسالة اولاً**")
    if replied_user.id == 7182427468:
        return await edit_delete(event, "**لا تحاول تنتحل المطور مطي!**")
    user_id = replied_user.id
    profile_pic = await event.client.download_profile_photo(user_id, Config.TEMP_DIR)
    first_name = html.escape(replied_user.first_name)
    if first_name is not None:
        first_name = first_name.replace("\u2060", "")
    last_name = replied_user.last_name
    if last_name is not None:
        last_name = html.escape(last_name)
        last_name = last_name.replace("\u2060", "")
    if last_name is None:
        last_name = "⁪⁬⁮⁮⁮⁮ ‌‌‌‌"
    replied_user = (await event.client(GetFullUserRequest(replied_user.id))).full_user
    user_bio = replied_user.about
    if user_bio is None:
        user_bio = ""
    fname = mid.first_name
    if fname == None:
        fname = ""
    lname = mid.last_name
    if lname == None:
        lname = ""
    oabout = me.about
    if oabout == None:
        oabout = ""
    addgvar("fname", fname)
    addgvar("lname", lname)
    addgvar("oabout", oabout)
    await event.client(functions.account.UpdateProfileRequest(first_name=first_name))
    await event.client(functions.account.UpdateProfileRequest(last_name=last_name))
    await event.client(functions.account.UpdateProfileRequest(about=user_bio))
    try:
        await event.client(functions.photos.UploadProfilePhotoRequest(file=await event.client.upload_file(profile_pic)))
    except Exception as e:
        delgvar("fname")
        delgvar("lname")
        delgvar("oabout")
        return await edit_delete(event, f"**فشل في الانتحال بسبب:**\n__{e}__")
    await edit_delete(event, "**⌁︙تـم نسـخ الـحساب بـنجاح ،✅**")
    if BOTLOG:
        await event.client.send_message(
            BOTLOG_CHATID,
            f"#الانتحال\nتم انتحال المستخدم: [{first_name}](tg://user?id={user_id })",
        )