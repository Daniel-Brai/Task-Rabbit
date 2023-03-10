from django.urls import path
from .views import (
    courier_index,
    courier_profile,
    courier_available_jobs,
    courier_available_job,
    courier_current_job,
    courier_current_job_camera,
    courier_job_completed,
    courier_archived_jobs,
    courier_payment_method,
)
from .apis import courier_available_jobs_api, courier_current_job_update_api, courier_fcm_token_update_api

app_name = "courier"

urlpatterns = [
    path("", courier_index, name="home"),
    path("profile/", courier_profile, name="profile"),
    path("payment/", courier_payment_method, name="payment"),
    path("jobs/", courier_available_jobs, name="available_jobs"),
    path("jobs/current/", courier_current_job, name="current_job"),
    path("jobs/completed/", courier_job_completed, name="completed_job"),
    path("jobs/archived/", courier_archived_jobs, name="archived_jobs"),
    path("jobs/<str:pk>/", courier_available_job, name="available_job_details"),
    path(
        "jobs/current/<str:pk>/camera/",
        courier_current_job_camera,
        name="current_job_camera",
    ),
    path("api/jobs/", courier_available_jobs_api, name="available_jobs_api"),
    path(
        "api/jobs/current/<str:pk>/update/",
        courier_current_job_update_api,
        name="current_job_update_api",
    ),
    path(
        "api/fcm-token/update/",
        courier_fcm_token_update_api,
        name="fcm_token_update_api",
    ),
]
