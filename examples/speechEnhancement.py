# bucket = 'my-bucket'
# s3_input_file = 'm2_script1_ipad_confroom1.wav'
# s3_output_file = 'm2_script1_ipad_confroom1-new.wav'
# output_content_type = 'wav'
# audo_api_key = 'c70f68814902e8705aa9d16ac84e91bf'
#
# # Generate Presigned URLs
# import boto3
# s3_client = boto3.client('s3')
# input_url = s3_client.generate_presigned_url(
#   'get_object',
#   Params={'Bucket': bucket, 'Key': s3_input_file}
# )
# output_url = s3_client.generate_presigned_url(
#   'put_object',
#   Params={
#   'Bucket': bucket,
#   'Key': s3_output_file,
#   'ContentType': output_content_type
#   },
#   HttpMethod='PUT'
# )
#
# # Remove Noise
# from time import sleep
# from audoai.noise_removal import NoiseRemovalClient
#
# noise_removal = NoiseRemovalClient(api_key=audo_api_key)
# job_id = noise_removal.create_job(input=input_url, output=output_url)
# noise_removal.wait_for_job_id(job_id)
#
# print('Noise removal complete. Waiting for upload...')
# sleep(2.0)
# print('Final result:', noise_removal.get_status(job_id))

from audoai.noise_removal import NoiseRemovalClient
noise_removal = NoiseRemovalClient(api_key='c70f68814902e8705aa9d16ac84e91bf')
result = noise_removal.process('data/m2_script1_ipad_confroom1.wav')
result.save('test.wav')
