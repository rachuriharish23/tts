from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('lJESHacN15ZehGNT7jj91a0oLHQKpyUMeesT9jyvU10A')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.eu-de.text-to-speech.watson.cloud.ibm.com/instances/81aa3d3f-e8cd-415a-a74a-9b8c5410c6bd')

with open('hello_world.wav', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            'Hello world',
            voice='en-US_AllisonV3Voice',
            accept='audio/wav'        
        ).get_result().content)
