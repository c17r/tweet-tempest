import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule, HttpClientXsrfModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { AppComponent } from './app.component';

import { TempestHeaderComponent } from './tempest/header/header.component';
import { TempestFormComponent } from './tempest/form/form.component';

@NgModule({
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    HttpClientXsrfModule.withOptions({
      cookieName: 'csrftoken',
      headerName: 'X-CSRFToken',
    })
  ],

  declarations: [
    TempestHeaderComponent,
    TempestFormComponent,

    AppComponent
  ],

  providers: [],

  bootstrap: [AppComponent]
})
export class AppModule { }
