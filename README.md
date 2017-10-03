# session2s3
Save your entire Python session to S3 with a simple function call

### Why?

Here are a few really good reasons to do this:
* **Fast debugging**. Why on earth does the database show results that you can't recreate by running the exact same script? Because when the script ran via cron at 3am the data was not the same as it is now (e.g. maybe a source table hadn't fully been updated yet at that time). Now you can inspect exactly what the script was taking in and putting out, without having had foresight as to what exactly you might need to debug or extra work logging inputs or intermediate values carefully
* **Straightforward disaster recovery**. Want to "roll back" a complicated change? Just find the session from the last time the script ran with good results, load it and run the final execution steps (e.g. an update statement) again. Voilá! Everything is as it was before
* **It's really easy**. And you don't have time to do something more customized

Since this captures the entire session, it keeps up with code changes- there's no extra step to follow through on when you add a new input table or column or change something about the process or its outputs. Just set it and forget it!

### Install and setup

You can use pip:
```
pip install session2s3
```

You will need your **AWS credentials** set in `~/.aws/credentials` as per the [boto3 instructions](https://boto3.readthedocs.io/en/latest/guide/quickstart.html#configuration)

```
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```

### Use

You can use this tool by simply adding the following to your script:

```
from session2s3 import session_to_s3

# insert all your clever code in between...

session_to_s3('my-project', 'my-bucket')
```

You're done!

Oops- the script produced some questionable results. Time to look into it. How do we load it into an interactive session?

First we browse with the AWS command line interface:
```
aws s3api list-objects --bucket 'my-bucket' --prefix 'my-project' --output text
```

When we see the latest one we download it thusly:
```
aws s3 cp s3://my_bucket/my-project_2017_08_25_20_48_24_011898.pkl ~/Downloads/debug.pkl
```

Now we open it using `dill` in Python:
```
import dill
# you may also need to import some of the packages your script uses

dill.load_session(~/Downloads/debug.pkl)

# now check it out...
dir()
```


### Extra credit

You could create a wrapper function for this so you don't have to include your bucket name every time. You could also opt to save only from production (so local testing doesn't clutter up your bucket) or skip the timestamps for example:

```
def workspace_to_s3(
  prefix,
  bucket_name="my-team-or-project-bucket",
  timestamp=True,
  save_from_local=False
  ):
  """Save session to S3 using team/project defaults."""
  sys = os.uname()[0]
  if sys == 'Linux' or save_from_local:
    filename = session_to_s3(prefix, bucket_name, timestamp)
    print "saved workspace " + filename + " to S3 bucket " + bucket_name
```
