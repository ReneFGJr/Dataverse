import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DoiInputComponent } from './doi-input.component';

describe('DoiInputComponent', () => {
  let component: DoiInputComponent;
  let fixture: ComponentFixture<DoiInputComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [DoiInputComponent]
    });
    fixture = TestBed.createComponent(DoiInputComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
