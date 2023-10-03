# Script: Executing Python code with Pytask

## How does pytask execute code

- I would leave it at these few points and purely focus on the mechanics for the rest of
  the screencast. Then mention, that the details will be in `what does pytask do`

Then switch to a live demo:

- Go to `epp_topics/src/python_basics/executing_pytask/screencast/example/`
- Show the contents of the two task files
- Run pytask (2 tasks should run)
- Run pytask again (no tasks should run)
  - Talk about how this can be useful in a project if you imagine the fist task is data
    management and the second is analysis
- Add more exclamation marks to task_write_world and run again (one task should run)
  - Mention how this carries over to the data management and analysis example

We don't talk about dependencies yet. An example with dependencies will by in what does
pytask do.
