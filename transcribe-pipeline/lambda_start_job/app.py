import boto3
import os
import time
from urllib.parse import unquote_plus

transcribe = boto3.client('transcribe')
OUTPUT_BUCKET = os.environ['OUTPUT_BUCKET']

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = unquote_plus(record['s3']['object']['key'])
        ext = key.split('.')[-1].lower()

        if ext not in ['mp3', 'mp4', 'wav', 'flac', 'ogg', 'amr', 'webm', 'm4a']:
            print(f"Formato não suportado: {key}")
            continue

        job_name = f"job-{key.replace('/', '-')}-{int(time.time())}"
        media_uri = f"s3://{bucket}/{key}"

        transcribe.start_transcription_job(
            TranscriptionJobName=job_name,
            Media={'MediaFileUri': media_uri},
            MediaFormat=ext,
            LanguageCode='pt-BR',
            OutputBucketName=OUTPUT_BUCKET,
            Settings={
                'ShowSpeakerLabels': True,
                'MaxSpeakerLabels': 4
            }
        )
        print(f"Transcription job '{job_name}' iniciado.")
