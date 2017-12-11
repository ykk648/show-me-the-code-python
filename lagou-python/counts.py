#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from page_info import job_info

while True:
    print(job_info.find().count())
    time.sleep(5)