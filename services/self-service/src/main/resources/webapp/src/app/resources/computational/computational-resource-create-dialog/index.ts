/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */

import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { MaterialModule } from '../../../shared/material.module';
import { FormControlsModule } from '../../../shared/form-controls';
import { ComputationalResourceCreateDialogComponent } from './computational-resource-create-dialog.component';
import { ComputationalResourceModel } from './computational-resource-create.model';
import { IsElementAvailablePipeModule, KeysPipeModule, UnderscorelessPipeModule } from '../../../core/pipes';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    FormControlsModule,
    KeysPipeModule,
    UnderscorelessPipeModule,
    MaterialModule,
    IsElementAvailablePipeModule
  ],
  declarations: [ComputationalResourceCreateDialogComponent],
  providers: [ComputationalResourceModel],
  entryComponents: [ComputationalResourceCreateDialogComponent],
  exports: [ComputationalResourceCreateDialogComponent]
})
export class ComputationalResourceCreateDialogModule {}
