import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MainComponent } from './010_tools/page/main/main.component';
import { RepatriationComponent } from './010_tools/widgat/repatriation/repatriation.component';

@NgModule({
  declarations: [
    AppComponent,
    MainComponent,
    RepatriationComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  schemeas:[CUSTOM_ELEMENTS_SCHEMA]
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
