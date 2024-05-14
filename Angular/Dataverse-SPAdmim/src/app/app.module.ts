import { NgModule, CUSTOM_ELEMENTS_SCHEMA, LOCALE_ID } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MainComponent } from './010_tools/page/main/main.component';
import { RepatriationComponent } from './010_tools/widgat/repatriation/repatriation.component';
import { HeaderModule } from './000_header/header/header.module';

@NgModule({
  declarations: [AppComponent, MainComponent, RepatriationComponent],
  imports: [BrowserModule, AppRoutingModule, HeaderModule],
  providers: [{ provide: LOCALE_ID, useValue: 'pt-BR' }],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
  bootstrap: [AppComponent],
})
export class AppModule {}
