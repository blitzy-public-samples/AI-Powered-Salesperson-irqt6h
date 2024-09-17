import dayjs from 'dayjs';

export function formatCurrency(amount: number, currencyCode: string): string {
  const formatter = new Intl.NumberFormat(undefined, {
    style: 'currency',
    currency: currencyCode,
  });
  return formatter.format(amount);
}

export function formatDate(date: string | number, format: string): string {
  return dayjs(date).format(format);
}

export function truncateText(text: string, maxLength: number): string {
  if (text.length <= maxLength) {
    return text;
  }
  return text.slice(0, maxLength - 3) + '...';
}