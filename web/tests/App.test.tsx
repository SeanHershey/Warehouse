import React from 'react';
import { render, screen } from '@testing-library/react';
import App from '../src/App';
import '@testing-library/jest-dom'
import "./App.css";

test('renders elements', () => {
    render(<App />);

    expect(screen.getByRole("heading")).toHaveTextContent(/Warehouse Shelves/);
    expect(screen.getByRole("button", { name: "name" })).toBeEnabled();
    expect(screen.getByRole("table")).toBeInTheDocument();
});