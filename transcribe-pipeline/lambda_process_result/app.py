import boto3
import json
import os
from urllib.request import urlopen

s3 = boto3.client('s3')
transcribe = boto3.client('transcribe')
OUTPUT_BUCKET = os.environ['OUTPUT_BUCKET']

def lambda_handler(event, context):
    job_name = event['detail']['TranscriptionJobName']
    job = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    uri = job['TranscriptionJob']['Transcript']['TranscriptFileUri']

    with urlopen(uri) as r:
        data = json.loads(r.read())

    transcript_text = data['results']['transcripts'][0]['transcript']

    output_key = f"processed/{job_name}.txt"
    s3.put_object(
        Bucket=OUTPUT_BUCKET,
        Key=output_key,
        Body=transcript_text.encode('utf-8')
    )

    print(f"Transcrição salva em s3://{OUTPUT_BUCKET}/{output_key}")
