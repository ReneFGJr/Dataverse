import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { HeaderRoutingModule } from './header-routing.module';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { NavbarComponent } from './navbar/navbar.component';


@NgModule({
  declarations: [HeaderComponent, FooterComponent, NavbarComponent],
  imports: [CommonModule, HeaderRoutingModule],
  exports: [HeaderComponent, FooterComponent, NavbarComponent],
})
export class HeaderModule {}
