import boto3

def lambda_handler(event, context):
    polly = boto3.client('polly', region_name='ap-south-1')
    s3 = boto3.client('s3', region_name='ap-south-1')

    text = "Keep your city clean. Do not throw garbage on the road."

    response = polly.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId='Aditi'
    )

    audio_stream = response['AudioStream'].read()
    response['AudioStream'].close()

    s3.put_object(
        Bucket='polly-audio-output-megha',
        Key='speech.mp3',
        Body=audio_stream,
        ContentType='audio/mpeg'
    )

    return {
        'statusCode': 200,
        'body': 'Speech generated successfully'
    }
