from django.shortcuts import HttpResponseRedirect, reverse


# create form that execute the specified command
# then return the log
def execute_command(request, device_pk, command_pk):
    print("ici", request, command_pk, device_pk)
    # if (request.GET.get('exec_btn')):
    #     pass # call function
    return HttpResponseRedirect(
        reverse(
            f"io_ssh:execute_command",
            kwargs={"device_pk": device_pk, "command_pk": command_pk},
        )
    )
